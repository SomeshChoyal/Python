class KnapsackSolver:
    def __init__(self, weights: List[int], values: List[int], capacity: int):
        """
        Initializes the KnapsackSolver object.

        Args:
            weights (List[int]): List of item weights.
            values (List[int]): List of item values.
            capacity (int): Maximum weight the knapsack can hold.

        Raises:
            ValueError: If input lists are empty or lengths are not equal.
        """
        if not weights or not values or len(weights) != len(values):
            raise ValueError("Weights and values lists must be non-empty and of equal length.")
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.max_value = 0
        self.selected_items = []

    def solve_knapsack(self) -> Tuple[int, List[int]]:
        """
        Solves the 0/1 knapsack problem and returns the maximum value and selected items.

        Returns:
            Tuple[int, List[int]]: Maximum value and list of indices of selected items.
        """
        dp = [[0 for _ in range(self.capacity + 1)] for _ in range(len(self.weights) + 1)]

        for i in range(1, len(self.weights) + 1):
            for w in range(self.capacity + 1):
                if self.weights[i - 1] <= w:
                    dp[i][w] = max(
                        self.values[i - 1] + dp[i - 1][w - self.weights[i - 1]], dp[i - 1][w]
                    )
                else:
                    dp[i][w] = dp[i - 1][w]

        self.max_value = dp[len(self.weights)][self.capacity]

        # Reconstruction of the items included in the knapsack
        i, w = len(self.weights), self.capacity
        while i > 0 and w > 0:
            if dp[i][w] != dp[i - 1][w]:
                self.selected_items.append(i - 1)
                w -= self.weights[i - 1]
            i -= 1

        return self.max_value, self.selected_items


def solve_knapsack(weights: List[int], values: List[int], capacity: int) -> Tuple[int, List[int]]:
    """
    Solves the 0/1 knapsack problem and returns the maximum value and selected items.

    Args:
        weights (List[int]): List of item weights.
        values (List[int]): List of item values.
        capacity (int): Maximum weight the knapsack can hold.

    Returns:
        Tuple[int, List[int]]: Maximum value and list of indices of selected items.
    """
    knapsack_solver = KnapsackSolver(weights, values, capacity)
    return knapsack_solver.solve_knapsack()


if __name__ == '__main__':
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    max_value, selected_items = solve_knapsack(weights, values, capacity)

    print("Maximum value:", max_value)
    print("Selected items:", selected_items)
