import subprocess

target = input("Enter target: ")
packets = int(input("Enter number of packets to send: "))

result = subprocess.run(["ping", "-n", str(packets), target], capture_output=True)

output = result.stdout.decode()
words = output.split()

if result.returncode == 0:
    print("Ping command successful")
else:
    print("Ping command failed")

latencies = []

for word in words:
     if word.startswith("time="):
        parts = word.split("=")
        value = parts[1]
        latency = int(value.removesuffix("ms"))
        latencies.append(latency)


if len(latencies) > 0:
    print("Latencies:", latencies)
    minimum = min(latencies)
    maximum = max(latencies)
    avg = sum(latencies) / len(latencies)

    print(f"Minimum latency: {minimum} ms")
    print(f"Maximum latency: {maximum} ms")
    print(f"Average latency: {avg:.2f} ms")
else:
    print("No latencies recorded")
   
print(f"Packets sent: {packets}")
received = len(latencies)
print(f"Packets received: {received}")

loss = packets - received
loss_percentage = (loss / packets) * 100
print(f"Packet loss: {loss_percentage:.2f}%")

if len(latencies) != 0:
    status = "ONLINE"
else:
    status = "OFFLINE"

print(status)
    