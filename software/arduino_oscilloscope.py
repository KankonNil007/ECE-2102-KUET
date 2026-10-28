
import serial
import matplotlib.pyplot as plt
import time

PORT = "COM3"
BAUD_RATE = 115200

SAMPLE_COUNT = 500
SAMPLE_INTERVAL = 0.01  # 10 ms, approximately 100 samples/s

VREF = 5.00
DIVIDER_FACTOR = 1.0  # Direct connection to A0; no voltage divider

TIME_WINDOW_MS = (SAMPLE_COUNT - 1) * SAMPLE_INTERVAL * 1000

ser = serial.Serial(PORT, BAUD_RATE, timeout=3)
time.sleep(2)
ser.reset_input_buffer()

plt.ion()
fig, ax = plt.subplots(figsize=(10, 5))
line, = ax.plot([], [], linewidth=1.2)

ax.set_title("ECE-2102 IR Pulse Detector")
ax.set_xlabel("Time (ms)")
ax.set_ylabel("Voltage (V)")
ax.set_xlim(0, TIME_WINDOW_MS)
ax.set_ylim(0, VREF)
ax.grid(True, alpha=0.4)

print("Oscilloscope running. Keep your finger still.")

try:
    while plt.fignum_exists(fig.number):
        text = ser.readline().decode(
            "ascii", errors="ignore"
        ).strip()

        if text != "BEGIN":
            continue

        readings = []

        while len(readings) < SAMPLE_COUNT:
            text = ser.readline().decode(
                "ascii", errors="ignore"
            ).strip()

            if text == "END":
                break

            try:
                value = int(text)
                if 0 <= value <= 1023:
                    readings.append(value)
            except ValueError:
                continue

        if len(readings) != SAMPLE_COUNT:
            continue

        volts = [
            value * VREF / 1023.0 * DIVIDER_FACTOR
            for value in readings
        ]

        time_ms = [
            i * SAMPLE_INTERVAL * 1000
            for i in range(SAMPLE_COUNT)
        ]

        line.set_data(time_ms, volts)

        low, high = min(volts), max(volts)
        margin = max((high - low) * 0.25, 0.03)

        ax.set_ylim(
            max(0, low - margin),
            min(VREF * DIVIDER_FACTOR, high + margin)
        )

        fig.canvas.draw_idle()
        fig.canvas.flush_events()
        plt.pause(0.001)

except KeyboardInterrupt:
    print("Stopped.")

finally:
    ser.close()
    plt.close("all")
