import os
from kili.client import Kili
import json
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('KILI_API_KEY')

kili = Kili(api_key=api_key)


class BoundingBox:
    def __init__(self,vertices) -> None:
        self.vertices = vertices
        pass

    def area(self):
        width = abs(self.vertices[2]['x'] - self.vertices[0]['x'])
        height = abs(self.vertices[2]['y'] - self.vertices[0]['y'])
        return width * height

class Annotations:
    def __init__(self, category, bounding_box):
        self.category = category
        self.bounding_box = bounding_box

    def to_dict(self):
        return {
            'category': self.category,
            'area': self.bounding_box.area()
        }

class Label:
    def __init__(self, label_id, annotations):
        self.label_id = label_id
        self.annotations = annotations  # list of Annotation objects

    def compute_areas(self):
        result = {'id': self.label_id, 'asterixs': [], 'obelixs': []}
        for ann in self.annotations:
            if ann.category.lower() == 'asterix':
                result['asterixs'].append(ann.bounding_box.area())
            elif ann.category.lower() == 'obelix':
                result['obelixs'].append(ann.bounding_box.area())
        return result



labels = kili.labels(project_id='cm96t7aprd3gq015bggiz8rn2')


results = []
for line in labels:
    annotations = []
    for ann_data in line['jsonResponse']['OBJECT_DETECTION_JOB']['annotations']:
        category = ann_data['categories'][0]['name']
        vertices = ann_data['boundingPoly'][0]['normalizedVertices']
        bbox = BoundingBox(vertices)
        annotations.append(Annotations(category, bbox))
    label = Label(line['id'], annotations)
    results.append(label.compute_areas())


print(json.dumps(results,indent=4))

with open('results.json', 'w') as f:
    json.dump(results, f, indent=4)