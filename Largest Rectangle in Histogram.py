class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        index = 0
        while index < len(heights):
            if not stack or heights[stack[-1]] <= heights[index]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                area = heights[top_of_stack] * ((index-stack[-1]-1) if stack else index)
                max_area = max(area, max_area)
        while stack:
            top_of_stack = stack.pop()
            area = heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index)
            max_area = max(area, max_area)
        return max_area

    def largestRectangleArea2(self, heights):
        # Time limit exceeded
        if not heights:
            return 0
        max_area = heights[0]
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                height = min(heights[i: j+1])
                width = j - i + 1
                area = height * width
                if area > max_area:
                    max_area = area
        return max_area


if __name__ == "__main__":
    a = [2, 1, 5, 6, 2, 3]
    print(Solution().largestRectangleArea(a))
    b = [1, 1]
    print(Solution().largestRectangleArea(b))

