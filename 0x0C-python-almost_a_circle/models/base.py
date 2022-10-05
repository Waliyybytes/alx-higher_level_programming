#!/usr/bin/python3
"""
    creating a base class
"""
import json
import csv


class Base:
    """  base class definition """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class instantiation """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ format for sharing data"""
        if list_dictionaries is None:
            return "[]"
        l_json = json.dumps(list_dictionaries)
        return l_json

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json format to file"""
        filename = cls.__name__ + ".json"
        tmp = []
        if list_objs is not None:
            for obj in list_objs:
                tmp.append(cls.to_dictionary(obj))
        with open(filename, 'w') as f:
            json.dump(cls.to_json_string(tmp), f, ensure_ascii=False)

    @staticmethod
    def from_json_string(json_string):
        """ from json string """
        return list(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ from dictionary to instance"""
        if cls.__name__ == "Square":
            tmp = cls(1)
        elif cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        tmp = []
        try:
            with open(filename, 'r') as f:
                tmp = cls.from_json_string(f.read())
                for i in range(len(tmp)):
                    tmp[i] = cls.create(**tmp[i])
        except Exception:
            pass
        return tmp

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to csv file"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            write_csv = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    write_csv.writerow([obj.id, obj.width,
                                        obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    write_csv.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """ load from a csv file"""
        filename = cls.__name__ + ".csv"
        tmp = []
        try:
            with open(filename, "r") as f:
                read_csv = csv.reader(f)
                for row in read_csv:
                    if cls.__name__ == "Rectangle":
                        csv_dict = {"id": int(row[0]),
                                    "width": int(row[1]),
                                    "height": int(row[2]),
                                    "x": int(row[3]),
                                    "y": int(row[4])}
                    elif cls.__name__ == "Square":
                        csv_dict = {"id": int(row[0]),
                                    "size": int(row[1]),
                                    "x": int(row[2]),
                                    "y": int(row[3])}
                    obj = cls.create(**csv_dict)
                    tmp.append(obj)
        except Exception:
            pass
        return tmp
