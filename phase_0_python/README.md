Phase 0 – Python Core (10 tasks)
Goal: Be able to write clean .py pipeline code.

    -1. Implement a @timer decorator and apply it  to  3 different functions (data load, train, evaluate).
    -2. Write a class Dataset with __init__, __repr__, __len__, __getitem__ that wraps a pandas DataFrame.        
    -3. Implement your own train_test_split using pure Python indices.
    -4. Write a generator batch_generator(X, y, batch_size) that yields mini-batches.
    -5. Show deep vs shallow copy using lists/dicts and prove difference via mutation.
    -6. Parse a JSON config (paths, model params) and dynamically build objects from it.
    -7. Implement exception-safe file I/O with custom DataValidationError.
    -8. Implement a simple Logger class with levels (INFO, WARN, ERROR) that logs to file.
    -9. Add 3 unit tests using unittest or pytest for your utility functions.
    -10. Build a CLI with argparse for python train.py --config config.json.
