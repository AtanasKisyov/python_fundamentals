import re


runners = {runner: 0 for runner in input().split(', ')}

data = input()

reg_distance = r"\d"

reg_runner = r"[a-zA-Z]"

while not data == "end of race":
    distance = [int(i) for i in re.findall(reg_distance, data)]
    runner = ''.join(re.findall(reg_runner, data))
    if runner in runners:
        runners[runner] += sum(distance)
    data = input()

sorted_runners = dict(sorted(runners.items(), key=lambda x: x[1], reverse=True))
winners = [w for w in sorted_runners.keys()]

print(f"1st place: {winners[0]}\n"
      f"2nd place: {winners[1]}\n"
      f"3rd place: {winners[2]}")
