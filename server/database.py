import embedder as embedder
from ComparatorResult import ComparatorResult
import data_loader
import os

__data = []
__comparator = embedder.cosineSimilarity
__comparator_result = ComparatorResult.LARGER_IS_BETTER

def initialize(products):
    for p in products:
        add_entry(p)

def set_comparator(comparator, comparator_result):
    global __comparator 
    global __comparator_result
    __comparator = comparator
    __comparator_result = comparator_result

def add_entry(data : str | object):
    dataStr = ""
    if isinstance(data, str):
        dataStr = data
    else:
        for key, value in data.items():
            if key == "feature":
                dataStr += value + ' '
            else:
                dataStr += key + ' '  + value + ' '
    vector = embedder.create_embedding(dataStr)
    #data['vector'] = vector
    #__data.append(data)
    __data.append({'vector' : vector, 'data' : data})

def get_all_entries():
    result = []
    for this_entry in __data:
        data = dict.copy(this_entry['data'])
        data['vector'] = this_entry['vector'].tolist()
        result.append(data)
    return result

def get_entry_count():
    return len(__data)

def similarity_search(vect, count = 5):
    if __comparator == None:
        raise Exception("Comparator cannot be None")
    
    # Iterate through all the vectors and perform a calculation on the distance from "vect"
    # to that vector, performing an insertion sort into the results array for each result 
    # and keeping the result to the maximum count
    results = []
    for this_vector in __data:
        compare_result = __comparator(vect, this_vector['vector'])
        inserted = False
        for idx, data in enumerate(results):
            if compare_result * __comparator_result.value > data[0] * __comparator_result.value:
                results.insert(idx, (compare_result, this_vector))
                if len(results) > count:
                    results.pop(count)
                inserted = True
                break
        if not inserted and len(results) < count:
            results.append((compare_result, this_vector))
    return results
