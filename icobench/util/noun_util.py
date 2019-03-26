import random
from .str_util import StrUtil
class NounUtil():

    WORDS = ["ability", "abroad", "abuse", "access", "accident", "account", "act", "action", "active", "activity",
              "actor", "addition", "address", "administration", "adult", "advance", "advantage", "advice", "affair",
              "affect", "afternoon", "age", "agency", "agent", "agreement", "air", "airline", "airport", "alarm",
              "alcohol", "alternative", "ambition", "amount", "analysis", "analyst", "anger", "angle", "animal",
              "annual", "answer", "anxiety", "anybody", "anything", "anywhere", "apartment", "appeal", "appearance",
              "apple", "application", "appointment", "area", "argument", "arm", "army", "arrival", "art", "article",
              "aside", "aspect", "assignment", "assist", "assistance", "assistant", "associate", "association",
              "assumption", "atmosphere", "attack", "attempt", "attention", "attitude", "audience", "author", "average",
              "award", "awareness", "baby", "back", "background", "bag", "bake", "balance", "ball", "band", "bank",
              "bar", "base", "baseball", "basis", "basket", "bat", "bath", "bathroom", "battle", "beach", "bear",
              "beat", "beautiful", "bed", "bedroom", "beer", "bell", "belt", "bench", "bend", "benefit", "bet",
              "beyond", "bicycle", "bid", "big", "bike", "bill", "bird", "birth", "birthday", "bit", "bite", "bitter",
              "black", "blame", "blank", "blind", "block", "blood", "blow", "blue", "board", "boat", "body", "bone",
              "bonus", "book", "boot", "border", "boss", "bother", "bottle", "bottom", "bowl", "box", "boy",
              "boyfriend", "brain", "branch", "brave", "bread", "break", "breakfast", "breast", "breath", "brick",
              "bridge", "brief", "brilliant", "broad", "brother", "brown", "brush", "buddy", "budget", "bug",
              "building", "bunch", "burn", "bus", "business", "button", "buy", "buyer", "cabinet", "cable", "cake",
              "calendar", "call", "calm", "camera", "camp", "campaign", "can", "cancel", "cancer", "candidate",
              "candle", "candy", "cap", "capital", "car", "card", "care", "career", "carpet", "carry", "case", "cash",
              "cat", "catch", "category", "cause", "celebration", "cell", "chain", "chair", "challenge", "champion",
              "championship", "chance", "change", "channel", "chapter", "character", "charge", "charity", "chart",
              "check", "cheek", "chemical", "chemistry", "chest", "chicken", "child", "childhood", "chip", "chocolate",
              "choice", "church", "cigarette", "city", "claim", "class", "classic", "classroom", "clerk", "click",
              "client", "climate", "clock", "closet", "clothes", "cloud", "club", "clue", "coach", "coast", "coat",
              "code", "coffee", "cold", "collar", "collection", "college", "combination", "combine", "comfort",
              "comfortable", "command", "comment", "commercial", "commission", "committee", "common", "communication",
              "community", "company", "comparison", "competition", "complaint", "complex", "computer", "concentrate",
              "concept", "concern", "concert", "conclusion", "condition", "conference", "confidence", "conflict",
              "confusion", "connection", "consequence", "consideration", "consist", "constant", "construction",
              "contact", "contest", "context", "contract", "contribution", "control", "conversation", "convert", "cook",
              "cookie", "copy", "corner", "cost", "count", "counter", "country", "county", "couple", "courage",
              "course", "court", "cousin", "cover", "cow", "crack", "craft", "crash", "crazy", "cream", "creative",
              "credit", "crew", "criticism", "cross", "cry", "culture", "cup", "currency", "current", "curve",
              "customer", "cut", "cycle", "dad", "damage", "dance", "dare", "dark", "data", "database", "date",
              "daughter", "day", "dead", "deal", "dealer", "dear", "death", "debate", "debt", "decision", "deep",
              "definition", "degree", "delay", "delivery", "demand", "department", "departure", "dependent", "deposit",
              "depression", "depth", "description", "design", "designer", "desire", "desk", "detail", "development",
              "device", "devil", "diamond", "diet", "difference", "difficulty", "dig", "dimension", "dinner",
              "direction", "director", "dirt", "disaster", "discipline", "discount", "discussion", "disease", "dish",
              "disk", "display", "distance", "distribution", "district", "divide", "doctor", "document", "dog", "door",
              "dot", "double", "doubt", "draft", "drag", "drama", "draw", "drawer", "dream", "dress", "drink", "drive",
              "driver", "drop", "drunk", "due", "dump", "dust", "duty", "ear", "earth", "ease", "east", "eat",
              "economics", "economy", "edge", "editor", "education", "effect", "effective", "efficiency", "effort",
              "egg", "election", "elevator", "emergency", "emotion", "emphasis", "employ", "employee", "employer",
              "employment", "energy", "engine", "engineer", "entertainment", "enthusiasm", "entrance", "entry",
              "environment", "equal", "equipment", "equivalent", "error", "escape", "essay", "establishment", "estate",
              "estimate", "evening", "event", "evidence", "exam", "examination", "example", "exchange", "excitement",
              "excuse", "exercise", "exit", "experience", "expert", "explanation", "expression", "extension", "extent",
              "external", "extreme", "eye", "face", "fact", "factor", "fail", "failure", "fall", "familiar", "family",
              "fan", "farm", "farmer", "fat", "father", "fault", "fear", "feature", "fee", "feed", "feedback", "feel",
              "female", "few", "field", "fight", "figure", "file", "fill", "film", "final", "finance", "finger",
              "finish", "fire", "fish", "fix", "flight", "floor", "flow", "flower", "fly", "focus", "fold", "food",
              "foot", "football", "force", "forever", "formal", "fortune", "foundation", "frame", "freedom", "friend",
              "friendship", "front", "fruit", "fuel", "fun", "function", "funeral", "funny", "future", "gain", "game",
              "gap", "garage", "garbage", "garden", "gas", "gate", "gather", "gear", "gene", "general", "gift", "girl",
              "girlfriend", "give", "glad", "glass", "glove", "go", "goal", "god", "gold", "golf", "good", "government",
              "grab", "grade", "grand", "grandfather", "grandmother", "grass", "great", "green", "grocery", "ground",
              "group", "growth", "guarantee", "guard", "guess", "guest", "guidance", "guide", "guitar", "guy", "habit",
              "hair", "half", "hall", "hand", "handle", "hang", "harm", "hat", "hate", "head", "health", "heart",
              "heavy", "height", "hell", "hello", "help", "hide", "high", "highlight", "highway", "hire", "historian",
              "history", "hit", "hold", "hole", "holiday", "home", "homework", "honey", "hook", "hope", "horror",
              "horse", "hospital", "host", "hotel", "hour", "house", "housing", "human", "hunt", "hurry", "hurt",
              "husband", "ice", "idea", "ideal", "if", "illegal", "image", "imagination", "impact", "implement",
              "importance", "impress", "impression", "improvement", "incident", "income", "increase", "independence",
              "independent", "indication", "individual", "industry", "inevitable", "inflation", "influence",
              "information", "initial", "initiative", "injury", "insect", "inside", "inspection", "inspector",
              "instance", "instruction", "insurance", "intention", "interaction", "interest", "internal",
              "international", "internet", "interview", "introduction", "investment", "invite", "iron", "island",
              "issue", "it", "item", "jacket", "job", "join", "joint", "joke", "judge", "judgment", "juice", "jump",
              "junior", "jury", "keep", "key", "kick", "kid", "kill", "kind", "king", "kiss", "kitchen", "knee",
              "knife", "knowledge", "lab", "lack", "ladder", "lady", "lake", "land", "landscape", "language", "laugh",
              "law", "lawyer", "lay", "layer", "lead", "leader", "leadership", "league", "leather", "leave", "lecture",
              "leg", "length", "lesson", "let", "letter", "level", "library", "lie", "life", "lift", "light", "limit",
              "line", "link", "lip", "list", "listen", "literature", "load", "loan", "local", "location", "lock", "log",
              "long", "look", "loss", "love", "low", "luck", "lunch", "machine", "magazine", "mail", "main",
              "maintenance", "major", "make", "male", "mall", "man", "management", "manager", "manner", "manufacturer",
              "many", "map", "march", "mark", "market", "marriage", "master", "match", "mate", "material", "math",
              "matter", "maximum", "maybe", "meal", "measurement", "meat", "media", "medicine", "medium", "meet",
              "meeting", "member", "membership", "memory", "mention", "menu", "mess", "message", "metal", "method",
              "middle", "midnight", "might", "milk", "mind", "mine", "minimum", "minor", "minute", "mirror", "miss",
              "mission", "mistake", "mix", "mixture", "mobile", "mode", "model", "mom", "moment", "money", "monitor",
              "month", "mood", "morning", "mortgage", "most", "mother", "motor", "mountain", "mouse", "mouth", "move",
              "movie", "mud", "muscle", "music", "nail", "name", "nasty", "nation", "national", "native", "natural",
              "nature", "neat", "necessary", "neck", "negative", "negotiation", "nerve", "net", "network", "news",
              "newspaper", "night", "nobody", "noise", "normal", "north", "nose", "note", "nothing", "notice", "novel",
              "nurse", "object", "objective", "obligation", "occasion", "offer", "office", "officer", "official", "oil",
              "one", "operation", "opinion", "opportunity", "opposite", "option", "orange", "order", "ordinary",
              "organization", "original", "other", "outcome", "outside", "oven", "owner", "pace", "pack", "package",
              "page", "pain", "paint", "pair", "panic", "paper", "parent", "park", "parking", "part", "particular",
              "partner", "party", "pass", "passage", "passenger", "passion", "past", "path", "patience", "patient",
              "pattern", "pause", "pay", "payment", "peace", "peak", "pen", "penalty", "pension", "people",
              "percentage", "perception", "performance", "period", "permission", "permit", "person", "personal",
              "personality", "perspective", "phase", "philosophy", "phone", "photo", "phrase", "physical", "physics",
              "piano", "pick", "picture", "pie", "piece", "pin", "pipe", "pitch", "pizza", "plan", "plane", "plant",
              "plastic", "plate", "platform", "play", "player", "pleasure", "plenty", "poem", "poet", "poetry", "point",
              "police", "policy", "politics", "pollution", "pool", "pop", "population", "position", "positive",
              "possession", "possibility", "possible", "post", "pot", "potato", "potential", "pound", "power",
              "practice", "preference", "preparation", "presence", "present", "presentation", "president", "press",
              "pressure", "price", "pride", "priest", "primary", "principle", "print", "prior", "priority", "private",
              "prize", "problem", "procedure", "produce", "product", "profession", "professional", "professor",
              "profile", "profit", "program", "progress", "project", "promise", "promotion", "prompt", "proof",
              "property", "proposal", "protection", "psychology", "public", "pull", "punch", "purchase", "purple",
              "purpose", "push", "put", "quality", "quantity", "quarter", "queen", "question", "quiet", "quit", "quote",
              "race", "radio", "rain", "raise", "range", "rate", "ratio", "raw", "reach", "reaction", "read", "reality",
              "reason", "reception", "recipe", "recognition", "recommendation", "record", "recover", "red", "reference",
              "reflection", "refrigerator", "refuse", "region", "register", "regret", "regular", "relation",
              "relationship", "relative", "release", "relief", "remote", "remove", "rent", "repair", "repeat",
              "replacement", "reply", "report", "representative", "republic", "reputation", "request", "requirement",
              "research", "reserve", "resident", "resist", "resolution", "resolve", "resort", "resource", "respect",
              "respond", "response", "responsibility", "rest", "restaurant", "result", "return", "reveal", "revenue",
              "review", "revolution", "reward", "rice", "rich", "ride", "ring", "rip", "rise", "risk", "river", "road",
              "rock", "role", "roll", "roof", "room", "rope", "rough", "round", "routine", "row", "royal", "rub",
              "ruin", "rule", "run", "rush", "sad", "safe", "safety", "sail", "salad", "salary", "sale", "salt",
              "sample", "sand", "sandwich", "satisfaction", "save", "savings", "scale", "scene", "schedule", "scheme",
              "school", "science", "score", "scratch", "screen", "screw", "script", "sea", "search", "season", "seat",
              "secret", "secretary", "section", "sector", "security", "selection", "self", "sell", "senior", "sense",
              "sensitive", "sentence", "series", "serve", "service", "session", "set", "sex", "shake", "shame", "shape",
              "share", "she", "shelter", "shift", "shine", "ship", "shirt", "shock", "shoe", "shoot", "shop", "shot",
              "shoulder", "show", "shower", "sick", "side", "sign", "signal", "signature", "significance", "silly",
              "silver", "simple", "singer", "single", "sink", "sir", "sister", "site", "situation", "size", "skill",
              "skin", "skirt", "sky", "sleep", "slice", "slide", "slip", "smell", "smile", "smoke", "snow", "society",
              "sock", "soft", "software", "soil", "solid", "solution", "somewhere", "son", "song", "sort", "sound",
              "soup", "source", "south", "space", "spare", "speaker", "special", "specialist", "specific", "speech",
              "speed", "spell", "spend", "spirit", "spiritual", "spite", "split", "sport", "spot", "spray", "spread",
              "spring", "square", "stable", "staff", "stage", "stand", "standard", "star", "start", "state",
              "statement", "station", "status", "stay", "steak", "steal", "step", "stick", "still", "stock", "stomach",
              "stop", "storage", "store", "storm", "story", "strain", "stranger", "strategy", "street", "strength",
              "stress", "stretch", "strike", "string", "strip", "stroke", "structure", "struggle", "student", "studio",
              "stuff", "stupid", "style", "subject", "substance", "success", "suck", "sugar", "suggestion", "suit",
              "summer", "sun", "supermarket", "support", "surgery", "surprise", "surround", "survey", "suspect",
              "sweet", "swim", "switch", "sympathy", "system", "table", "tackle", "tale", "talk", "tank", "tap",
              "target", "task", "taste", "tax", "tea", "teach", "teacher", "team", "tear", "technology", "telephone",
              "television", "tell", "temperature", "temporary", "tennis", "tension", "term", "test", "text", "thanks",
              "theme", "theory", "thing", "thought", "throat", "ticket", "tie", "till", "tip", "title", "today", "toe",
              "tomorrow", "tone", "tongue", "tonight", "tool", "tooth", "top", "topic", "total", "touch", "tough",
              "tour", "tourist", "towel", "tower", "town", "track", "trade", "tradition", "traffic", "train", "trainer",
              "transition", "transportation", "trash", "travel", "treat", "tree", "trick", "trip", "trouble", "truck",
              "trust", "truth", "try", "tune", "turn", "twist", "two", "type", "uncle", "union", "unique", "unit",
              "university", "upper", "upstairs", "use", "user", "usual", "vacation", "valuable", "value", "variation",
              "variety", "vast", "vegetable", "vehicle", "version", "video", "view", "village", "virus", "visit",
              "visual", "voice", "volume", "wait", "wake", "walk", "wall", "war", "wash", "watch", "water", "wave",
              "way", "weakness", "wealth", "wear", "weather", "web", "wedding", "week", "weekend", "weight", "weird",
              "welcome", "west", "western", "wheel", "whereas", "white", "whole", "wife", "will", "win", "wind",
              "window", "wine", "wing", "winner", "winter", "wish", "witness", "woman", "wonder", "wood", "word",
              "worker", "world", "worry", "worth", "wrap", "writer", "yard", "year", "yellow", "yesterday", "you",
              "young", "youth", "zone"];


    def get_random_word(self):
        len_words = len(self.WORDS) - 1
        return self.WORDS[random.randint(0, len_words)]


    def get_random_title(self):
        len_words = len(self.WORDS) - 1
        first = self.WORDS[random.randint(0, len_words)]
        second = self.WORDS[random.randint(0, len_words)]
        while first == second:
            second = self.WORDS[random.randint(0, len_words)]

        first = first[0:len(first)-2]+StrUtil().get_random_letters(2)
        second = second[0:len(second) - 2]+StrUtil().get_random_letters(2)
        app_name = first+" "+second
        short_name = self.get_short_name(first,second)
        title = {'title': app_name,'short_name': short_name}
        return title

    def get_short_name(self, fist, second):
        len_first = len(fist) - 1
        len_second = len(second) - 1

        if len_first >4:
            len_first =random.randint(3, 4)
        if len_second >4:
            len_second =random.randint(3, 4)

        return fist[0:len_first]+second[0:len_second]



if __name__ == '__main__':
    print(NounUtil().get_short_name("Alan",None))




















