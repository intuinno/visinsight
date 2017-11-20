import json
import cPickle as pickle
import argparse

def addComment(cDict, image_index, c):
    if image_index not in cDict:
        cDict[image_index] = []
    cDict[image_index].append(c)
        
def main(args):
    qa_pairs_path = args.question_path
    with open(qa_pairs_path) as qa_fp:
        qa = json.load(qa_fp)
    qa_pairs = qa['qa_pairs']
    cDict = {}
    
    for q in qa_pairs:
        if q['question_id'] == 0:
            if q['answer'] == 1:
                c = '%s is the minimum.'%q['color1_name']
                addComment(cDict, q['image_index'], c)
        elif q['question_id'] == 1:
            if q['answer'] == 1:
                c = '%s is the maximum.'%q['color1_name']
                addComment(cDict, q['image_index'], c)
        elif q['question_id'] == 2:
            if q['answer'] == 1:
                c = '%s is less than the %s.'%(q['color1_name'], q['color2_name'])
                addComment(cDict, q['image_index'], c)
        elif q['question_id'] == 3:
            if q['answer'] == 1:
                c = '%s is greater than the %s.'%(q['color1_name'], q['color2_name'])
                addComment(cDict, q['image_index'], c)
        elif q['question_id'] == 4:
            if q['answer'] == 1:
                c = '%s is the low median.'%q['color1_name']
                addComment(cDict, q['image_index'], c)
        elif q['question_id'] == 5:
            if q['answer'] == 1:
                c = '%s is the high median.'%q['color1_name']
                addComment(cDict, q['image_index'], c)
        elif q['question_id'] == 6:
            if q['answer'] == 1:
                c = '%s has the minimum area under curve.'%q['color1_name']
                addComment(cDict, q['image_index'], c)
        elif q['question_id'] == 7:
            if q['answer'] == 1:
                c = '%s has the maximum area under curve.'%q['color1_name']
                addComment(cDict, q['image_index'], c)
        elif q['question_id'] == 8:
            if q['answer'] == 1:
                c = '%s is the smoothest.'%q['color1_name']
                addComment(cDict, q['image_index'], c)
        elif q['question_id'] == 9:
            if q['answer'] == 1:
                c = '%s is the roughest.'%q['color1_name']
                addComment(cDict, q['image_index'], c)
        elif q['question_id'] == 10:
            if q['answer'] == 1:
                c = '%s has the lowest value.'%q['color1_name']
                addComment(cDict, q['image_index'], c)
        elif q['question_id'] == 11:
            if q['answer'] == 1:
                c = '%s has the highest value.'%q['color1_name']
                addComment(cDict, q['image_index'], c)
        elif q['question_id'] == 12:
            if q['answer'] == 1:
                c = '%s is less than %s.'%(q['color1_name'], q['color2_name'])
                addComment(cDict, q['image_index'], c)
        elif q['question_id'] == 13:
            if q['answer'] == 1:
                c = '%s is greater than %s.'%(q['color1_name'], q['color2_name'])
                addComment(cDict, q['image_index'], c)
        elif q['question_id'] == 14:
            if q['answer'] == 1:
                c = '%s intersects %s.'%(q['color1_name'], q['color2_name'])
                addComment(cDict, q['image_index'], c)

    with open(args.insight_path, 'wb') as f:
        pickle.dump(cDict, f)
        print "Saved insights to %s"%args.insight_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--insight_path', type=str,
                       default='./insight.json',
                       help='path for saving generated insights list')
    parser.add_argument('--question_path', type=str,
                       default='./data/sample_train1/qa_pairs.json',
                       help='path for qa_pairs.json file')
    args = parser.parse_args()
    main(args)
