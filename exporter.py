from drugs_for_disease_dict import DrugsForDiseaseDict


class Exporter:
    dicts = {}

    def add_to_export(self, name, dict):
        self.dicts[name] = dict

    def export(self):
        nodes = []
        links = []
        pre_nodes = {}
        pre_links = []
        for key in self.dicts:
            ## export nodes
            disease_node = Node(key, 0, key)
            pre_nodes[key] = disease_node
            for med in self.dicts[key]:
                if med not in pre_nodes:
                    pre_nodes[med] = Node(med, 1, med)
            ## end export nodes
            ## export links
            for med in self.dicts[key]:
                pre_links.append(Link(key, med, self.dicts[key][med]))
            ## end export links
        
        for node in pre_nodes:
            nodes.append(pre_nodes[node].to_string())
        for link in pre_links:
            links.append(link.to_string())

        with open("export.js", mode="w") as file:
           file.write("var nodes = [")
           
           first = True
           for write_node in nodes:
               if first:
                   file.write(write_node + "\n")
                   first = False
               else:
                   file.write("," + write_node + "\n")

           file.write("]")
           file.write("var links = [")
           
           first = True
           for write_link in links:
               if first:
                   file.write(write_link + "\n")
                   first = False
               else:
                   file.write("," + write_link + "\n")
           file.write("]")

class Node:
    id = ""
    group = 1
    label = ""
    def __init__(self, node_id, node_group, node_label):
        self.id = node_id
        self.group = node_group
        self.label = node_label

    def to_string(self):
        pre_string = "id: '{}' , group: {} , label: '{}'".format(self.id, self.group, self.label)
        return "{" + pre_string + "}"

class Link:
    target = ""
    source = ""
    strength  = 0
    def __init__(self, node_target, node_source, node_strength):
        self.target = node_target
        self.source = node_source
        self.strength = node_strength

    def to_string(self):
        pre_string = "target: '{}' , source: '{}' , strength: '{}'".format(self.target, self.source, self.strength)
        return "{" + pre_string + "}"
