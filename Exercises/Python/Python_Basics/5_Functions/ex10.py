'''
Similar to the previous exercise, write a function that extracts the region code from a locale. For example:
'''

def extract_region(local):
    return local.split('_')[1][0:2]

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR
