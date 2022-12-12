class SafeArray{
    public:
        // Constructor
        SafeArray(int);
        // Destructor
        ~SafeArray();

        int get(int);
        void set(int, int);

        int length;

    private:
        int *_array;

        bool isSafe(int i);
};