import json, os, datetime

DATA_DIR = "data"

def load_json(name, default):
    path = os.path.join(DATA_DIR, name)
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(name, obj):
    path = os.path.join(DATA_DIR, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

def main():
    posts  = load_json("posts.json", [])
    shows  = load_json("shows.json", [])
    brands = load_json("brands.json", [])

    # TODO: тут будет сбор новых данных из источников
    # MVP: просто “heartbeat”, чтобы Actions работал и ты видел коммиты при изменениях

    meta = {
        "updatedAt": datetime.datetime.utcnow().isoformat() + "Z",
        "postsCount": len(posts),
        "showsCount": len(shows),
        "brandsCount": len(brands),
    }
    save_json("_meta.json", meta)

if __name__ == "__main__":
    main()
