class Calculate:
    @staticmethod
    def calculate_node_sum(node):
        return Calculate.__wrapper_node_sum(node, 0)

    @staticmethod
    def __wrapper_node_sum(node, total_sum):
        total_sum += node.val

        if node.get_left() is not None:
            total_sum = Calculate.__wrapper_node_sum(node.get_left(), total_sum)

        if node.get_right() is not None:
            total_sum = Calculate.__wrapper_node_sum(node.get_right(), total_sum)

        return total_sum

    @staticmethod
    def calculate_node_average(node):
        return Calculate.__wrapper_node_average(node, 0, 0, True)

    @staticmethod
    def __wrapper_node_average(node, total_sum, counts, top):
        counts += 1
        total_sum += node.val

        if node.get_left() is not None:
            total_sum, counts = Calculate.__wrapper_node_average(node.get_left(), total_sum, counts, False)

        if node.get_right() is not None:
            total_sum, counts = Calculate.__wrapper_node_average(node.get_right(), total_sum, counts, False)

        if top:
            return total_sum / counts

        return total_sum, counts

    @staticmethod
    def calculate_node_median(node):
        return Calculate.__wrapper_node_median(node, [], True)

    @staticmethod
    def __wrapper_node_median(node, val_list, top):
        val_list.append(node.val)

        if node.get_left() is not None:
            val_list = Calculate.__wrapper_node_median(node.get_left(), val_list, False)

        if node.get_right() is not None:
            val_list = Calculate.__wrapper_node_median(node.get_right(), val_list, False)

        if top:
            val_list.sort()
            mid = int(len(val_list) / 2)

            if len(val_list) % 2 == 1:
                return val_list[mid]

            return (val_list[mid] + val_list[mid - 1]) / 2

        return val_list
