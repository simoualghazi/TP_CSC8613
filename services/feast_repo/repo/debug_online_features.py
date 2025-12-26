from feast import FeatureStore

def main():
    store = FeatureStore(repo_path="/repo")

    user_id = "9305-CDSKC"  # adapte

    features = [
        "subs_profile_fv:months_active",
        "subs_profile_fv:monthly_fee",
        "subs_profile_fv:paperless_billing",
    ]

    feature_dict = store.get_online_features(
        features=features,
        entity_rows=[{"user_id": user_id}],
    ).to_dict()

    print("Online features for user:", user_id)
    print(feature_dict)

if __name__ == "__main__":
    main()
