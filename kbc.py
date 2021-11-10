# print("welcome","🙏🙏")
# print("lest play kon banega crorpati (KBC)")
# print("😻😻","😻😻","😻😻","😻😻","😻😻")
# question_list = [
#     "1 How many continents are there?",             
#     "2 What is the capital of India?",            
#     "3 NG mei kaun se course padhaya jaata hai?"    ]
# options_list = [
#     ["Four", "Nine", "Seven", "Eight"],
#     ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#     ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
# ]
# def kbc(question_list,options_list,solution_list,ans):
#     # def question(que):
#     i=0
#     a=0
#     b=1
#     count=0
#     while i<len(question_list):
#         def question(que):
#             return(question_list[i])
#             j=0
#             c=1
#             while j<=len(options_list):
#                 print(c,".",options_list[i][j])
#                 j+=1
#                 c+=1
            
#             # ans=["3 Seven","4 Eight","4 Delhi","3 Chennai","1 Software Engineering","2 Counseling"]
#             print("you have 1 life line ","5️⃣","0️⃣","--","5️⃣","0️⃣")
#             print("do you want life line")
#             print("🎤 say" )
#             life_line=input("yes or no  ")
#             if life_line=="yes":
#                 if count==0:
#                     print(ans[i+a])
#                     print(ans[i+b])
#                     print("😉😉")
#                     answer=int(input("enter your answer "))
#                     if solution_list[i]==answer:
#                         print("right")
#                         print("😍😍","✅","😍😍")
#                         print("congrects")
#                         print("play forword","🎮🎮")
#                         count+=1
#                     else:
#                         print("wrong","🙀🙀")
#                         print("😧😧")
#                         print("game over","😵😵")
#                         break/
#                 else:
#                     print("you don't have life line ")
#                     print("you already used your life line","◀️")
#                     a=int(input("enter answer "))
#                     if solution_list[i]==a:
#                         print("right")
#                     else:
#                         print("wrong","🙀🙀")
#                         print("game over","😵😵")
#                         print("😧😧")


#                         break
#             elif life_line=="no":
#                 print("👆👆")
#                 user=int(input("chose answer from obave options "))
#                 if solution_list[i]==user:
#                     print("right")
#                     print("😍😍")
#                     print("you win you got 10,000 rupees")
#                     print("😉😉")
#                 else:
#                     print("wrong")
#                     print("😫😫")
#                     print("🙀🙀")
#                     # break
#             else:
#                 print("wrong","😫😫")
#                 print("🥴🥴")
#                 print("game over","🤦🏻‍♀️","🤦🏻‍♀️","🤦🏻‍♀️")
#                 print("😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭")
#                 # break
#             a+=1
#             b+=1
#             i+=1
# kbc(["1 How many continents are there?","2 What is the capital of India?","3 NG mei kaun se course padhaya jaata hai?"],[["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#     ["Software Engineering", "Counseling", "Tourism", "Agriculture"]],[3, 4, 1],["3 Seven","4 Eight","4 Delhi","3 Chennai","1 Software Engineering","2 Counseling"])



# question=
# def kbc(question_list,options_list,solution_list):
#     for i in range (0,len(question_list),1):
#         def quetion(que):
#             return(que[i])
#         print(quetion[i])
#         def options(op):
#             for j in range(0,len(op)+1):
#                 print(op[i][j])
#             life_line=input("enetr do you want life line yes or no ")
#             if life_line=="yes":
#                 return(op[i][0],op[i][2])
#             elif life_line=="no":
#                 return("=-o-i8u")
#         print(option([["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]])
#         def solution_list(an):
#             if an==solution_list[i]:
#                 print("right answer ")
#             else:
#                 return("wrong ")
#         # print()
# kbc(["1 How many continents are there?",             
#     "2 What is the capital of India?",            
#     "3 NG mei kaun se course padhaya jaata hai?"],[
#     ["Four", "Nine", "Seven", "Eight"],
#     ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#     ["Software Engineering", "Counseling", "Tourism", "Agriculture"]],[3, 4, 1])





quetion=["1 How many continents are there?","2 What is the capital of India?","3 NG mei kaun se course padhaya jaata hai?"]
money=0
def kbc(quetion,answer,OPTION,money,count):
    for process in range(0,len(quetion)):
        def quetion(que):
            return(que[process])
        print(quetion(["1 How many continents are there?","2 What is the capital of India?","3 NG mei kaun se course padhaya jaata hai?"]))
        def options(opt):
            for i in range(0,len(opt)+1):
                print(opt[process][i])
            life_line=input("5050")
            if life_line=="yes":
                return(opt[process][0],opt[process][2])
            else:
                return"---------"
        print(options([["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]]))
        def answer(ans):
            if ans==answer[process]:
                print("right")
            else:
                return("wrong")
        print(answer(input("enternkdnckjdjjnnc:").lower()))
kbc(["1 How many continents are there?","2 What is the capital of India?","3 NG mei kaun se course padhaya jaata hai?"],[3, 4, 1],[
    ["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]],0,0)
print("you won",money)