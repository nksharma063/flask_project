# import os
# from pathlib import Path
# import time

# def readConfig(path, file):
#     dir = os.path.isdir(path)
#     if not dir:
#         print("Please enter the valid directory")
#     else:
#         for name in os.scandir():
#             if name.is_file():
#                 return file
            
# print(readConfig('D:\\DevOps_HerVired\\flask_project\\flask_project', 'server.yml'))
#     # file = os.path.isfile(os.path.join(path, file))

#     # file = os.path.isfile(os.path.join(path, file))
#     #     print("The specified directory", path," does not exist")
#     # elif not os.path.isfile(os.path.join(path, file))
#     #     print("The specified file", file, "does not exist")
#     # else:
#     #     return file

# # dir_path = Path("./")
# # for name in dir_path.iterdir():



# print(readConfig('D:\DevOps_HerVired\flask_project\flask_project', 'server.yml'))




# # print(os.listdir())  It works like string value list aeverythings
# # print(os.path.isfile('server.yml'))


    

# # def readConfig(abc):
# #     return os.path.isdir('abc')
        
    

            

# # print(readConfig('D:\DevOps_HerVired\flask_project\flask_project'))






# # import os,fileinput


# # def database():
# #     database = {}
# #     server = {}
# #     with fileinput.input(files=('database.yml','server.yml'), inplace=False, backup='', mode = 'r', encoding = "utf-8") as f:
 
# #         for line in f:
# #             # key, value = line.strip().split('=')
# #             proces                 
                
# #             if (f.filename() == 'database.yml') and (each not in database):
# #                 database['key']=value
                 
# #             elif (f.filename() == 'server.yml') and (each not in server):
# #                     server['key']=value
# #             else:
# #                     print("Ruko zara")
# #     return database, server
#         # database, configuration = f
#         # print(database, configuration)

# #       with open(path/database.cfg, 'rw') as file:
# # #         file = file.readlines()
# # #         print(file)
# # # except:
# # #     raise "File not found , Please execute script in directory with configuration file"
    
# # print(database('D:\DevOps_HerVired\flask_project\flask_project\'))

# # print(database('D:\DevOps_HerVired\flask_project'))
# # print(database())