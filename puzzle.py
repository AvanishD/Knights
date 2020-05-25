from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."

# This is the statement of A
Asays = And(AKnight, AKnave)

knowledge0 = And(
    Or(And(AKnight, Not(AKnave)), And(Not(AKnight), AKnave)),
    Biconditional(Asays, AKnight)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.

# This is the statement of A
Asays = And(AKnave, BKnave)

# This is the statement of B
Bsays = Symbol('')

knowledge1 = And(
    Or(And(AKnight, Not(AKnave)), And(Not(AKnight), AKnave)),
    Biconditional(Asays, AKnight),
    Or(And(BKnight, Not(BKnave)), And(Not(BKnight), BKnave)),
    Biconditional(Bsays, BKnight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

# This is the statement of A
Asays = Or(And(BKnave, AKnave), And(BKnight, AKnight))

# This is the statement of B
Bsays = Or(And(BKnave, AKnight), And(AKnave, BKnight))

knowledge2 = And(
    Or(And(AKnight, Not(AKnave)), And(Not(AKnight), AKnave)),
    Or(And(BKnight, Not(BKnave)), And(Not(BKnight), BKnave)),
    Biconditional(Asays, AKnight),
    Biconditional(Bsays, BKnight)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

# This is the statement of A
Asays = Or(AKnight, AKnave)

# This is the statement of B
Bsays = And(Symbol(Asays==AKnave), CKnave)

# This is the statement of C
Csays = AKnight

knowledge3 = And(
    Or(And(AKnight, Not(AKnave)), And(Not(AKnight), AKnave)),
    Biconditional(Asays, AKnight),
    Or(And(BKnight, Not(BKnave)), And(Not(BKnight), BKnave)),
    Biconditional(Bsays, BKnight),
    Or(And(CKnight, Not(CKnave)), And(Not(CKnight), CKnave)),
    Biconditional(Csays, CKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
