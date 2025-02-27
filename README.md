# 📚 BookVerse

## 📖 Project Overview
This project is a book recommendation system that utilizes the k-Nearest Neighbors (KNN) algorithm to suggest books based on genre and average ratings. Users can input a preferred genre, and the system returns a list of recommended books.

## 📂 Folder Structure
```
book_recommendation_project/
├── Bookverse.ipynb          # Jupyter Notebook containing the implementation
├── Dataset/                 # Stores book dataset
│   ├── dataset.csv          # Book data (Book_ID, Genre, Rating, etc.)
├── .gitignore               # Ignores unnecessary Python files
├── LICENSE                  # Apache 2.0 license
├── README.md                # Project documentation
```

## 🚀 How to Use
### **1️⃣ Install Dependencies**
Ensure you have Python installed, then install the required libraries:
```bash
pip install pandas scikit-learn numpy openpyxl
```

### **2️⃣ Run the Project**
Execute the **BookVerse.ipynb** script:
```
Kernel -> Python
jupyter nbconvert --to notebook --execute Bookverse.ipynb
```

### **3️⃣ Select Genre & Get Recommendations**
1. The system will prompt you to choose a genre:
   - Fantasy
   - Romance
   - Fiction
   - Mystery
2. After entering a genre, the system returns a list of recommended books ranked by rating.

## 📜 License
This project is licensed under the Apache License 2.0.

---
📌 **Happy Reading!** 📖✨

