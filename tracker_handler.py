from deep_sort_realtime.deepsort_tracker import DeepSort

def init_tracker():
    return DeepSort(max_age=30)
