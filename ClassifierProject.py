
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# Definisikan base models
base_models = [
    (
        'rf',
        RandomForestClassifier(
            n_estimators=50,
            random_state=42
        )
    ),

    (
        'svm',
        SVC(
            kernel='rbf',
            probability=True,
            random_state=42
        )
    ),

    (
        'knn',
        KNeighborsClassifier(
            n_neighbors=5
        )
    ),

    (
        'dt',
        DecisionTreeClassifier(
            max_depth=5,
            random_state=42
        )
    )
]

# Meta-learner (biasanya simple model)
meta_learner = LogisticRegression(
    max_iter=1000
)

# Stacking Classifier
stacking = StackingClassifier(
    estimators=base_models,
    final_estimator=meta_learner,
    cv=5,  # cross-validation untuk generate meta-features
    stack_method='predict_proba'
)

stacking.fit(X_train, y_train)
stacking_pred = stacking.predict(X_test)

# Bandingkan semua metode
print("=" * 50)
print("PERBANDINGAN SEMUA METODE")
print("=" * 50)

print(f"Single Decision Tree : {accuracy_score(y_test, dt_pred):.4f}")
print(f"Bagging : {accuracy_score(y_test, bagging_pred):.4f}")
print(f"Random Forest : {accuracy_score(y_test, rf_pred):.4f}")
print(f"AdaBoost : {accuracy_score(y_test, ada_pred):.4f}")
print(f"Gradient Boosting : {accuracy_score(y_test, gb_pred):.4f}")
print(f"Stacking : {accuracy_score(y_test, stacking_pred):.4f}")

# Visualisasi perbandingan
models = [
    'DT',
    'Bagging',
    'RF',
    'AdaBoost',
    'GB',
    'Stacking'
]

scores = [
    accuracy_score(y_test, dt_pred),
    accuracy_score(y_test, bagging_pred),
    accuracy_score(y_test, rf_pred),
    accuracy_score(y_test, ada_pred),
    accuracy_score(y_test, gb_pred),
    accuracy_score(y_test, stacking_pred)
]

plt.figure(figsize=(10, 5))

plt.bar(
    models,
    scores,
    color=[
        'blue',
        'green',
        'red',
        'orange',
        'purple',
        'brown'
    ]
)

plt.ylabel('Accuracy')
plt.title('Perbandingan Akurasi : Single Model vs Ensemble')

plt.ylim(0.9, 1.0)

for i, v in enumerate(scores):
    plt.text(
        i,
        v + 0.002,
        f'{v:.4f}',
        ha='center'
    )

plt.show()