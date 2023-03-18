def task(keyboard, nums_in_text, nums_in_text_id):
    transition = 0

    for idx in range(1, nums_in_text):
        ch_1 = nums_in_text_id[idx - 1]
        ch_2 = nums_in_text_id[idx]

        transition += keyboard[ch_1] != keyboard[ch_2]

    return transition


_ = int(input())
keyboard = dict(
    zip(map(int, input().split()), map(int, input().split()))
)
nums_in_text = int(input())
nums_in_text_id = list(map(int, input().split()))

print(task(keyboard, nums_in_text, nums_in_text_id))
