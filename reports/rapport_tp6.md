# TP6:CI/CD pour systèmes ML + réentraînement automatisé + promotion MLflow

## OUALGHAZI Mohamed

### Exercice 1:
![alt text](image-75.png)
![alt text](image-76.png)
![alt text](image-77.png)

### Exercice 2:
![alt text](image-78.png)
**Question 2.d:**  
On extrait une fonction “pure” (sans I/O, sans dépendance à Prefect/MLflow) pour pouvoir la tester rapidement et de manière déterministe, sans avoir à démarrer la stack Docker ni dépendre d’un état externe (registry, réseau, base de données).

### Exercice 3:

![alt text](image-79.png)
![alt text](image-80.png)
On utilise un delta pour éviter de promouvoir un modèle sur un gain insignifiant dû au hasard (split, bruit des données, variance de l’algorithme).
### Exercice 4:
![alt text](image-81.png)
![alt text](image-82.png)

### Exercice 5:
![alt text](image-83.png)
L’API doit être redémarrée car le modèle MLflow models:/streamflow_churn/Production est chargé au démarrage et mis en mémoire ; si une nouvelle version est promue en Production après coup, l’API ne la recharge pas automatiquement sans redémarrage.

### Exercice 6:
