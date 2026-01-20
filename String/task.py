name=input("Enter String:")
part1=(name[-2:])
part2=(name[2:len(name)-2])

part3=(name[:-7])


print(f"Output: {part1+part2+part3}")