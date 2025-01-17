#1

matrix1 = [
    [2, 3, 2],
    [4, 7, 6],
    [7, 8, 6]]
matrix2 = [
    [2, 8, 7],
    [6, 2, 4],
    [1, 6, 1]]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]
for i in range(3):
    print(i)
    for j in range(3):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
for k in result:
    #print(k)

#2

# i=input("Enter a string:")
# joined_string = ''.join(i.split()).lower()
# if (joined_string==joined_string[::-1]):
#     print("The string is palindrome.")
# else :
#     print("The string is not palindrome.")

