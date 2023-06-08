from LinkedList import LinkedList

if __name__ == "__main__":
    l_list = LinkedList(10)

    print("Head: ", l_list.get_head())

    l_list.insert_before_head(2)

    print("Head: ", l_list.get_head())

    l_list.insert_end(22)

    print("Whole list: ", l_list.print_list())
