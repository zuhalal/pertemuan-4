# Naming Convention (Standar Penamaan)

# flatcase (sangat tidak direkomendasikan)
# thisisvariable = "inivariabel"

# SCREAMCASE (sangat cocok untuk digunakan sebagai nama konstanta)
# THISISVARIABLE = "INIVARIABEL"

# camelCase (sangat sering dipakai dan dinilai lebih mudah diketik dan dibaca)
# thisIsVariable = "iniVariabel"

# snake_case (cocok untuk menuliskan nama file atau directory)
# this_is_variable = "ini_variabel"



# Python Syntax
# Menggunakan indentation (tab) dan tidak menggunakan curly bracket (kurung kurawal)

# number = 10
# name = "dono"

# if number < 0:
#     print(number)
#     name = "kasino"
#     print(name)

# print(name)



# Python Variable

# Dynamically Type (Memiliki Tipe Data Sesuai Keadaan)

# x = 1
# print(x, "=", type(x))

# y ="johny"
# print(y, "=", type(y))

# x = "1"
# print(x, "=", type(x))

# z = str(2)
# print(z, "=", type(z))

# X = '2'
# print(X, '!=', x)

# Multiple Assignment/Unpacking Data (Memasukkan Nilai Sekaligus)

# x, y, z = 3, "oke", 4.0
# print(x, "=", type(x))
# print(y, "=", type(y))
# print(z, "=", type(z))

# x = y = z = 10
# print(x, "=", y, "=", z)

# data = [3, "oke", 4.0]
# p, q, r = data
# print(p, q, r)

# Scope (Jangkauan)

# Menggunakan Global Variabel di dalam Function
# firstVariable = "hello"

# def firstScopeFunction():
#     print(firstVariable)

# firstScopeFunction()

# print(firstVariable)

# # Menggunakan Local Variabel di luar Function

# def secondScopeFunction():
    # global secondVariable
    # secondVariable = "world"
    # print(secondVariable)

# secondScopeFunction()

# print(secondVariable)