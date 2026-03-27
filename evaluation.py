import pandas as pd
from detector import detect_ai

# Dataset location
CSV_PATH = r"C:\Users\nidhi\OneDrive\Desktop\Oakland Uni\Winter 2026\Artificial Intelligence (CSI-4130)\AI Detector App\data\ai_human.csv"

# Column names
TEXT_COLUMN = "text"
LABEL_COLUMN = "generated"

# Number of samples to test
MAX_SAMPLES = 10


def load_dataset():
    df = pd.read_csv(CSV_PATH)
    sample_size = min(MAX_SAMPLES, len(df))
    df = df.sample(n=sample_size, random_state=42)
    return df


def evaluate():

    df = load_dataset()

    correct = 0
    total = len(df)
    results = []

    true_human_pred_human = 0
    true_human_pred_ai = 0
    true_ai_pred_human = 0
    true_ai_pred_ai = 0

    for i, row in df.iterrows():

        text = str(row[TEXT_COLUMN])[:2000]
        label_value = row[LABEL_COLUMN]

        if label_value == 1:
            true_label_str = "AI Generated"
        else:
            true_label_str = "Human Written"

        result = detect_ai(text)
        pred_label = result["label"]
        score = result["score"]

        if pred_label == true_label_str:
            correct += 1

        if true_label_str == "Human Written" and pred_label == "Human Written":
            true_human_pred_human += 1
        elif true_label_str == "Human Written" and pred_label == "AI Generated":
            true_human_pred_ai += 1
        elif true_label_str == "AI Generated" and pred_label == "Human Written":
            true_ai_pred_human += 1
        elif true_label_str == "AI Generated" and pred_label == "AI Generated":
            true_ai_pred_ai += 1

        results.append({
            "true_label": true_label_str,
            "pred_label": pred_label,
            "score": score
        })

        print(f"True: {true_label_str} | Pred: {pred_label} | Score: {score:.2f}")

    accuracy = correct / total

    print("\nFinal Results")
    print("-------------------")
    print(f"Total samples: {total}")
    print(f"Accuracy: {accuracy:.2%}")

    print("\nConfusion Matrix")
    print("-------------------")
    print(f"True Human  → Pred Human: {true_human_pred_human}")
    print(f"True Human  → Pred AI:    {true_human_pred_ai}")
    print(f"True AI     → Pred Human: {true_ai_pred_human}")
    print(f"True AI     → Pred AI:    {true_ai_pred_ai}")

    results_df = pd.DataFrame(results)
    results_df.to_csv("results/detection_results.csv", index=False)
    print("\nResults saved to results/detection_results.csv")


if __name__ == "__main__":
    evaluate()