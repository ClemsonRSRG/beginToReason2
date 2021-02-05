"""
Class that represents an attempt made by students.
"""


class Node:
    START_COLOR_CODE = "#9cffed"
    GAVE_UP_COLOR_CODE = "#f58787"
    CORRECT_COLOR_CODE = "#b3ffb0"
    CORRECT_ARROW_COLOR_CODE = "#08d100"
    MINIMUM_TO_BE_ANNOTATED = 5
    DEGENERATE_CODE = "degenerate"
    DECIMAL_PRECISION = 2
    START_NAME = "Start"
    GAVE_UP_NAME = "GaveUp"

    def __init__(self, attempt, is_correct):
        self.appearances = 0
        self.distance_sum = 0
        self.successful_appearances = 0
        self.attempt = attempt
        self.is_correct = is_correct
        self.node_list = dict()

    def add_next(self, next_node):
        if self.node_list.get(next_node):
            self.node_list[next_node] += 1
        else:
            self.node_list[next_node] = 1

    def calculate_goodness(self):
        if self.is_correct:
            return 2
        if self.attempt == self.GAVE_UP_NAME:
            return -1
        correct = total = 0
        for node in self.node_list:
            total += self.node_list[node]
            if node.is_correct:
                correct += self.node_list[node]
        return correct / total

    # Declaration of the node in plantUML code
    def print_declaration(self, minimum_appearances):
        if (self.appearances < minimum_appearances) & (self.attempt != self.GAVE_UP_NAME):
            return ""
        output = ["object \"" + str(self.attempt) + "\" as " + str(self.get_hash_code())]
        if self.attempt == self.START_NAME:
            output.append(" " + self.START_COLOR_CODE)
        elif self.attempt == self.GAVE_UP_NAME:
            output.append(" " + self.GAVE_UP_COLOR_CODE)
        elif self.is_correct:
            output.append(" " + self.CORRECT_COLOR_CODE)
        output.append("\n" + str(self.get_hash_code()) + " : appearances: " + str(self.appearances) + "\n")
        # distance
        if (not self.is_correct) & (self.attempt != self.GAVE_UP_NAME):
            if self.successful_appearances > 0:
                distance = str(self.distance_sum / self.successful_appearances)
                if len(distance) > 2 + self.DECIMAL_PRECISION:
                    distance = distance[0: 2 + self.DECIMAL_PRECISION]
                output.append(str(self.get_hash_code()) + " : distance: " + distance + "\n")
            else:
                output.append(str(self.get_hash_code()) + " : distance: " + str(self.DEGENERATE_CODE) + "\n")
        goodness = self.calculate_goodness()
        if (goodness <= 1) & (goodness >= 0):
            output.append(str(self.get_hash_code()) + " : score: " +
                      str(goodness + 0.5 * 10 ** -self.DECIMAL_PRECISION)[0: 2+self.DECIMAL_PRECISION] + "\n")
        return "".join(output)

    # prints the connections of the node in plantUML code
    def print_connections(self, minimum_appearances):
        if (self.appearances < minimum_appearances) & (self.attempt != self.GAVE_UP_NAME):
            return ""
        output = []
        for node in self.node_list:
            if (node.appearances >= minimum_appearances) | (node.attempt == self.GAVE_UP_NAME):
                output.append(str(self.get_hash_code()) + " -")
                if self.better_than(node):
                    output.append("down")
                else:
                    output.append("up")
                output.append("[thickness=" + str(self.node_list.get(node)))
                if node.is_correct:
                    output.append("," + self.CORRECT_ARROW_COLOR_CODE)
                output.append("]-> " + str(node.get_hash_code()))
                if self.node_list.get(node) >= self.MINIMUM_TO_BE_ANNOTATED:
                    output.append(": " + self.node_list.get(node))
                output.append("\n")
        return "".join(output)

    def return_family(self):
        return self.return_family_helper(set())

    def return_family_helper(self, already_found):
        already_found.add(self)
        for node in self.node_list:
            if node not in already_found:
                already_found = node.return_family_helper(already_found)
        return already_found

    def find_node(self, attempt):
        for node in self.return_family():
            if node.attempt == attempt:
                return node
        return None

    def add_appearance(self):
        self.appearances += 1

    def add_successful_appearance(self):
        self.successful_appearances += 1

    def add_distance(self, distance):
        self.distance_sum += distance

    def get_hash_code(self):
        return id(self)

    def better_than(self, other):
        if self.is_correct:
            return True
        if other.is_correct:
            return False
        if self.successful_appearances == 0:
            return False
        if other.successful_appearances == 0:
            return True
        return other.distance_sum / other.successful_appearances > self.distance_sum / self.successful_appearances