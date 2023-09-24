def get_ordered_dicts(keys=[], *lists):
    try:
        list_of_dicts = []
        if not lists:
            return list_of_dicts
        # notice incase of providing invalid keys not equal to lists
        if len(lists) != len(keys):
            raise ValueError("Keys and lists length not equal")
        
        # as previous check , checks for the length of the keys vs length of data lists , this check is deep 1 level it check for each list values and make sure all data lists have same length
        if len(set(list(map(lambda l : len(l), lists)))) > 1:
            raise ValueError("Data lists length not equal")
        
        zip_lists = list(zip(*lists))
        for l in zip_lists:
            list_of_dicts.append(dict(zip(keys, l)))

        return list_of_dicts
    except Exception as e:
        print("unknown error in get_ordered_dicts, {}".format(sys.exc_info()))
        raise e
