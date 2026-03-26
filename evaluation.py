import pandas as pd
from detector import detect_ai

# Path to the dataset CSV file
CSV_PATH = "ai_human.csv"

# Column names in the dataset
TEXT_COLUMN = "text"      # Text content
LABEL_COLUMN = "label"    # 0 = human, 1 = AI

# Limit number of samples to avoid too many API calls
MAX_SAMPLES = 40


def load_dataset():
    """
    Load dataset from CSV and randomly sample a subset.
    This helps reduce API usage and makes testing faster.
    """
    df = pd.read_csv(CSV_PATH)

    # Random sampling to avoid running detection on the entire dataset
    df = df.sample(n=MAX_SAMPLES, random_state=42)

    return df


def evaluate():
    """
    Evaluate Sapling AI detector on a labeled dataset.

    For each text sample:
    - Run AI detection
    - Compare predicted label with ground truth
    - Record prediction results

    Finally:
    - Compute overall accuracy
    """

    df = load_dataset()

    correct = 0
    total = len(df)

    # Store results for later analysis (e.g., CSV export or metrics)
    results = []

    for i, row in df.iterrows():

        # Extract text and true label from dataset
        text = row[TEXT_COLUMN]
        true_label = row[LABEL_COLUMN]

        # Convert numeric label to match Sapling output format
        # Sapling returns "AI Generated" or "Human Written"
        true_label_str = "AI Generated" if true_label == 1 else "Human Written"

        # Call Sapling AI detection API
        result = detect_ai(text)

        # Extract predicted label and score
        pred_label = result["label"]
        score = result["score"]   # Score is typically 0–100

        # Check if prediction matches ground truth
        if pred_label == true_label_str:
            correct += 1

        # Save result for this sample
        results.append({
            "id": i,
            "true_label": true_label_str,
            "pred_label": pred_label,
            "score": score
        })

        # Print per-sample result (useful for debugging and quick inspection)
        print(f"[{i}] True: {true_label_str} | Pred: {pred_label} | Score: {score:.2f}")

    # Compute accuracy
    accuracy = correct / total

    print("\nFinal results:")
    print(f"Total samples: {total}")
    print(f"Accuracy: {accuracy:.2f}")

    return results


if __name__ == "__main__":
    evaluate()
