from collections import deque

tools = deque([int(x) for x in input().split()])
substances = deque([int(x) for x in input().split()])
challenges = [int(x) for x in input().split()]

while challenges and substances:
    current_tool = tools.popleft()
    current_substance = substances[-1]

    result = current_tool * current_substance

    if result in challenges:
        challenges.remove(result)
        substances.pop()
        continue

    current_tool += 1
    tools.append(current_tool)
    substances[-1] -= 1
    if substances[-1] == 0:
        substances.pop()

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

else:
    print("Harry is lost in the temple. Oblivion awaits him.")


if tools:
    print(f"Tools: {', '.join(str(t) for t in tools)}")
if substances:
    print(f"Substances: {', '.join(str(s) for s in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(ch) for ch in challenges)}")
