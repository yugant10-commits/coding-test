def read_sentences(input_file):
    # """
    #     read the file contents and split them into 3 modules:
    #     ref_words: glob is I
    #     price_msgs: glob glob Silver is 34 Credits
    #     questions: how much is pish tegj glob glob ?
    #     error_msgs: not understandable msgs
    # """
    ref_words = []
    price_msgs = []
    questions = []
    error_msgs = []

    segmented_dict = {
        "ref_words": ref_words,
        "price_msgs": price_msgs,
        "questions": questions,
        "error_msgs": error_msgs,
    }
    msg = input_file.strip()
    with open(input_file) as f:
        for line in f:
            msg = line.strip()
            split_msg = msg.split()
            if split_msg[-1] == "?":
                questions.append(msg)
            elif split_msg[-1] == "Credits" and "is" in msg:
                price_msgs.append(msg)
            elif split_msg[-1] in "IVXLCDM" and "is" in msg:
                ref_words.append(msg)
            else:
                error_msgs.append(msg)
    return segmented_dict
