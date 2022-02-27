import os, sys, json, hashlib;

class JsonHelp:

    def load(self, path, default=None):
        if os.path.exists(path):
            return json.loads(open(path, "r").read());
        return default;
    def store(self, path, data_json):
        path_buffer = "/tmp/" + hashlib.md5(path.encode()).hexdigest();
        if os.path.exists(path_buffer):
            os.unlink(path_buffer);
        with open(path_buffer, "w") as f:
            f.write(json.dumps(data_json));
            f.close();
            os.rename(path_buffer, path);
            return True;
        return False;


