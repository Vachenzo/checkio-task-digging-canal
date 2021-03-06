"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [
                [1, 1, 1, 1, 0, 1, 1],
                [1, 1, 1, 1, 0, 0, 1],
                [1, 1, 1, 1, 1, 0, 1],
                [1, 1, 0, 1, 1, 0, 1],
                [1, 1, 0, 1, 1, 1, 1],
                [1, 0, 0, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1]],
            "answer": 2,
            "explanation": [[3, 3], [3, 4]]
        },
        {
            "input": [
                [0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 0, 1, 0, 1, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0]],
            "answer": 3,
            "explanation": [[1,2], [2, 2], [3, 2]]
        },
        {
            "input": [
                [1, 1, 1, 1, 1, 0, 1, 1],
                [1, 0, 1, 1, 1, 0, 1, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [1, 0, 1, 1, 1, 0, 1, 1],
                [0, 0, 1, 1, 0, 0, 0, 0],
                [1, 0, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 0, 1, 1, 1, 1]],
            "answer": 2,
            "explanation": [[0, 1], [7, 1]]
        },
        {
            "input": [
                [0, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 0, 1],
                [1, 1, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 1, 1, 0],
                [0, 1, 1, 1, 0, 0, 0, 0]
            ],
            "answer": 0,
            "explanation": []
        },
        {
            "input": [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]
            ],
            "answer": 1,
            "explanation": [[4, 0]]
        },
        {
            "input": [
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1]],
            "answer": 8,
            "explanation": [
                [0, 3],
                [1, 3],
                [2, 3],
                [3, 3],
                [4, 3],
                [5, 3],
                [6, 3],
                [7, 3]
            ]
        },
        {
            "input": [
                [1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1]
            ],
            "answer": 5,
            "explanation": [
                [0, 3],
                [2, 3],
                [4, 3],
                [6, 3],
                [8, 3]
            ]
        },
        {
            "input": [
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 0, 0, 1],
                [1, 1, 1, 1, 0, 1, 1, 1],
                [1, 1, 1, 0, 0, 1, 1, 1],
                [1, 0, 0, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1]
            ],
            "answer": 4,
            "explanation": [
                [0, 6],
                [2, 4],
                [4, 2],
                [6, 0]
            ]
        }
    ],
    "Extra": [
        {
            "input": [
                [1, 1, 1, 1, 0, 1, 1],
                [1, 1, 1, 1, 0, 0, 1],
                [1, 1, 1, 1, 1, 0, 1],
                [1, 1, 0, 0, 1, 0, 1],
                [1, 1, 0, 1, 1, 1, 1],
                [1, 0, 0, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1]
            ],
            "answer": 1,
            "explanation": [
                [3, 4]
            ]
        },
        {
            "input": [
                [0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 0, 0, 0, 1, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0]
            ],
            "answer": 3,
            "explanation": [
                [1, 3],
                [2, 3],
                [3, 3]
            ]
        },
        {
            "input": [
                [1, 1, 1, 1, 1, 0, 1, 1],
                [0, 1, 1, 1, 1, 0, 1, 1],
                [0, 0, 1, 0, 1, 0, 1, 0],
                [1, 0, 1, 1, 1, 0, 1, 1],
                [0, 0, 1, 1, 0, 0, 0, 0],
                [1, 0, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 0, 1, 1, 1, 1]
            ],
            "answer": 2,
            "explanation": [
                [0, 0],
                [7, 1]
            ]
        },
        {
            "input": [
                [0, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 0, 0, 0, 1, 1, 0],
                [0, 0, 0, 1, 0, 1, 1, 0],
                [0, 1, 1, 1, 0, 0, 0, 0]
            ],
            "answer": 0,
            "explanation": []
        },
        {
            "input": [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 0, 1, 1],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]
            ],
            "answer": 1,
            "explanation": [
                [4, 3]
            ]
        },
        {
            "input": [
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 0, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1]
            ],
            "answer": 7,
            "explanation": [
                [0, 3],
                [1, 3],
                [2, 3],
                [4, 3],
                [5, 3],
                [6, 3],
                [7, 3]
            ]
        },
        {
            "input": [
                [1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1]
            ],
            "answer": 4,
            "explanation": [
                [0, 3],
                [2, 3],
                [4, 3],
                [6, 3]
            ]
        },
        {
            "input": [
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 0, 0, 1],
                [1, 1, 1, 1, 0, 1, 1, 1],
                [1, 1, 1, 0, 0, 1, 1, 1],
                [1, 0, 0, 0, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1]
            ],
            "answer": 3,
            "explanation": [
                [0, 6],
                [2, 4],
                [6, 0]
            ]
        }
    ]
}
