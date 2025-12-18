# Cloud-Native Deployment Project (CA1 - B8IS124)

## What is this?

This is the project for Dereks Class, Cloud Platform Dev. The main goal here wasn't to build a super complex app, but to **set up the infrastructure and automation** for it.

Basically, it's a simple API running in the cloud, but the focus is on *how* it got there.

## Architecture (What I Used)

The project is 100% serverless and uses the following Google Cloud services:

*   **Cloud Run:** Where the app runs. Chosen because it's serverless and **scales to zero** (meaning it costs nothing when no one is using it).
*   **Firestore:** The NoSQL database. Simple and easy to connect with Cloud Run.
*   **Secret Manager:** To securely store the app's secret/token. **No passwords are in the code!**
*   **Cloud Build:** The CI/CD engine. It does all the automation work.

## How it works (CI/CD)

The deployment is fully automatic.

1.  I do a `git push` with the code here on GitHub.
2.  **Cloud Build** sees the push and starts working.
3.  It takes the `Dockerfile`, builds the app image.
4.  It saves the image to **Artifact Registry**.
5.  It deploys the image to **Cloud Run** using the `cloudbuild.yaml` file.

**Result:** The app is updated in the cloud without any manual steps from me.

## How to Test the App (Endpoints)

The API endpoints can be tested directly by accessing the Cloud Run URL in a web browser.

| Endpoint | Method | What it does |
| :--- | :--- | :--- |
| `/` | `GET` | Checks if the app is alive and if it loaded the secret. |
| `/items` | `POST` | Sends a JSON payload to save an item in Firestore. |
| `/items` | `GET` | Retrieves all saved items from Firestore. |

## Key Files

*   **`cloudbuild.yaml`:** The script that Cloud Build follows to automate the deployment.
*   **`Dockerfile`:** The recipe for packaging the app into a container.
*   **`requirements.txt`:** The Python dependencies (Flask, Firestore SDK).

---

**Live App Link:** [https://ca1-cloudrun-firestore-671505329776.europe-west1.run.app]
