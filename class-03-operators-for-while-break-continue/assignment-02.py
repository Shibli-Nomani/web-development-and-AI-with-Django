#assignment-02
# while loop: Loop will perform contineous printing and it will not stop. There must be a condition in case of while
# loop (ex: if/elif/else) to stop the interation. We use **break** to stop the loop and we use **continue** to skip certain condition.

# Here, we prepare a simple project for **CRUD** program using while loop, if, elif, else condition.

# assignment
# create list

create_list = ["John", "Jeni", "Andrew", "Christina", "Smith"]

while True:
    put_command = input("Type your desire command create / read / update / add / delete /  quite: ")
    if put_command == "quite":
        print("Congratulation!! You are done. your system is shutting down the program....")
        break  # stop the infinite loop once we type "quite"
    # create list
    elif put_command == "create":
        print("here is your create_list: ", create_list)
    # read only
    elif put_command == "read":
        print("your current create_list is : ", create_list)

    # update only
    elif put_command == "update":
        index_range = len(create_list) - 1
        print("your available index_range is: ", index_range)
        desired_index = int(input("type your desired index for update: "))

        if desired_index > index_range:
            print("your provided index is out of range. please use within the index_range {}"
                  .format(index_range))


        else:
            desired_name = input("type your desired new name for update: ")
            create_list[desired_index] = desired_name
            print("see the create_list after update: ", create_list)

            # add only
    elif put_command == "add":

        print("provide a name only")
        value = input("input your desire name for adding: ")
        create_list.append(value)
        print("see create_list after adding: ", create_list)

    # delete only
    elif put_command == "delete":
        print("here is the current list: ", create_list)
        name = input("to remove, type your desired name from the list: ")

        if name not in (create_list):
            print("incorrect input ! please provide correct name from the list")

        else:
            create_list.remove(value)
            print("your item has been dropped successfuly and here is your current create_list: ", create_list)


    else:
        print("Wrong Input!!")





