from datetime import datetime

print(datetime.now().second)


wait_until = (datetime.now().second + 2) % 60

while datetime.now().second != wait_until:
    print('Still waiting!')
    
print(f'We are at {wait_until} seconds!')