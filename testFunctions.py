# def min_to_hrs(min):
#     hr=min/60
#     return hr
# def sec_to_hrs(sec):
#     hr=(sec/3600)
#     return hr

# print(min_to_hrs(70))
# print(sec_to_hrs(7200))
# print(type(min_to_hrs(70)))
# print(type(sec_to_hrs(7200)))

# def minsec_to_hr(min,sec):
#     hr=min/60 + sec/3600
#     return hr

# def minsec_to_hr(sec,min=200):
#     hr=min/60 + sec/3600
#     return hr
def minsec_to_hr(min=90,sec=1800):
    hr=min/60 + sec/3600
    print(str(hr)+"______hihi")
    return hr

print(minsec_to_hr(70,300))
print(minsec_to_hr(3600))
minsec_to_hr()