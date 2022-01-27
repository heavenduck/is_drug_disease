import graphData.data as data

class Exporter:
    dicts = {}
    output_path = ""

    def __init__(self):
        self.output_path = "visual/data_own.js"

    def add_to_export(self, data_dict):
        self.dicts = data_dict

    def get_max_dict_value(self):
        max_dict_value = 0

        for disease in self.dicts:
            for drug in self.dicts[disease]:
                if self.dicts[disease][drug] > max_dict_value:
                    max_dict_value = self.dicts[disease][drug]

        return max_dict_value

    def export(self):

        nodes = []
        links = []
        pre_nodes = {}
        pre_links = []
        max_drug_occurrence = self.get_max_dict_value()

        for disease in self.dicts:

            # export nodes
            disease_node = Node(disease, 0, disease)
            pre_nodes[disease] = disease_node

            for drug in self.dicts[disease]:
                if drug not in pre_nodes:
                    pre_nodes[drug] = Node(drug, 1, drug)
            # end export nodes

            # export links
            for drug in self.dicts[disease]:

                strength = self.dicts[disease][drug] / max_drug_occurrence
                pre_links.append(Link(disease, drug, strength))
            # end export links

        for node in pre_nodes:
            nodes.append(pre_nodes[node].to_string())
        for link in pre_links:
            links.append(link.to_string())

        with open(self.output_path, mode="w") as file:
            file.write("var nodes = [")

            first = True
            for write_node in nodes:
                if first:
                    file.write(write_node + "\n")
                    first = False
                else:
                    file.write("," + write_node + "\n")

            file.write("] \n")
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
        pre_string = "id: \"{}\" , group: {} , label: \"{}\"".format(self.id, self.group, self.label)
        return "{" + pre_string + "}"


class Link:
    target = ""
    source = ""
    strength = 0

    def __init__(self, node_target, node_source, node_strength):
        self.target = node_target
        self.source = node_source
        self.strength = node_strength

    def to_string(self):
        pre_string = "target: \"{}\" , source: \"{}\" , strength: \"{}\"".format(self.target, self.source,
                                                                                 self.strength)
        return "{" + pre_string + "}"


if __name__ == "__main__":
    test_dict = data.get_data()

    exp = Exporter()
    exp.add_to_export(test_dict)
    exp.export()
