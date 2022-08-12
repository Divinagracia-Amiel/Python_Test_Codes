gifts = {1:'Partridge',
         2:'turtle doves',
         3:'french hens',
         4:'calling birds',
         5:'gold rings',
         6:'geese',
         7:'swans',
         8:'maids',
         9:'ladies',
         10:'lords',
         11:'pipers',
         12:'drummers'}
init = 12
total_gift = 0
gift = 1
key = 0
for i in range(1, init+1):
    total_gift += gift
    gift += 1
    key += 1
    print(f"{key}",gifts.get(key), ", ")
print(f"The total gifts are {total_gift} gifts")
