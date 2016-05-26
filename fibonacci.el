;;; package --- fibonacci algorithms
;;; Commentary:
;; reference scip
;; (fibonacci-v1 5)
;; (fibonacci-v2 5 1 0)
;; (fibonacci-v3 5 1 0 1 1 1 0)

;;; Code:
(defun fibonacci-v1 (n)
  "Fibonacci version 1, O(n2)
N order number"
  (cond ((zerop n) 0)
        ((= n 1) 1)
        (t (+ (fibonacci-v1 (1- n)) (fibonacci-v1 (- n 2))))))

(defun fibonacci-v2 (n a b)
  "Fibonacci version 2, O(n)
N order number
A init value 1
B init value 0"
  (cond ((zerop n) b)
        (t (fibonacci-v2 (1- n) (+ a b) a))))

(defun fibonacci-v3 (n a b p1 q1 p2 q2)
  "Fibonacci version 3, O(log2n)
suppose transform T
    a' = p1 x a + q1 x b
    b' = p2 x a + q2 x b
init p1 = 1, q1 = 1, p2 = 1, q2 = 0
then T^2
    a'' = p1 x a' + q1 x b'
        = p1 x (p1 x a + q1 x b) + q1 x (p2 x a + q2 x b)
        = (p1 x p1 + q1 x p2) x a + (p1 x q1 + q1 x q2) x b
    b'' = p2 x a' + q2 x b'
        = p2 x (p1 x a + q1 x b) + q2 x (p2 x a + q2 x b)
        = (p2 x p1 + q2 x p2) x a + (p2 x q1 + q2 x q2) x b
so
    p1' = p1 x p1 + q1 x p2
    q1' = p1 x q1 + q1 x q2
    p2' = p2 x p1 + q2 x p2
    q2' = p2 x q1 + q2 x q2
N order number
A init value 1
B init value 0
P1, Q1, P2, Q2 parameters"
  (cond ((zerop n) b)
        ((evenp n) (fibonacci-v3
                    (/ n 2)
                    a
                    b
                    (+ (* p1 p1) (* q1 p2))
                    (+ (* p1 q1) (* q1 q2))
                    (+ (* p2 p1) (* q2 p2))
                    (+ (* p2 q1) (* q2 q2))))
        (t (fibonacci-v3
            (1- n)
            (+ (* p1 a) (* q1 b))
            (+ (* p2 a) (* q2 b))
            p1
            q1
            p2
            q2))))

(provide 'fibonacci)
;;; fibonacci.el ends here
