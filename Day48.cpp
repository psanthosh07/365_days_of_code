int solve(vector<int> &A){
    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 0; i < A.size(); ++i) {
        pq.push(A[i]);
}
 int minCost = 0;

    while (pq.size() > 1) {
        int first = pq.top();
        pq.pop();
        int second = pq.top();
        pq.pop();

        int newRope = first + second;
        minCost += newRope;
        pq.push(newRope);
    }

    return minCost;
}
