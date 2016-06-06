;;; packages -- some algorithms about tree
;;; Commentary:
;; This is a collection of tree algorithms
;; tree is (cons value nodes), and nodes is (cons left-tree right-tree)
;; (tree-to-list '(4 . ((2 . ((1 . nil) . (3 . nil))) . (6 . ((5 . nil) . (7 . nil))))))
;; (travel-tree '(4 . ((2 . ((1 . nil) . (3 . nil))) . (6 . ((5 . nil) . (7 . nil))))) (lambda (x) (message "%d" x)) 'MID)

;;; Code:
(defun tree-to-list (tree)
  "Translate TREE to a list."
  (let ((value (car tree))
        (nodes (cdr tree)))
    (cond ((not value) nil)
          (t (append (tree-to-list (car nodes))
                     (list value)
                     (tree-to-list (cdr nodes)))))))

(defun travel-tree (tree func order)
  "Trace TREE, call FUNC by ORDER.
ORDER is the travel order, it may be 'PRE, 'MID, or 'SUF"
  (let ((value (car tree))
        (nodes (cdr tree)))
    (cond ((not value) nil)
          (t (cond ((eq order 'PRE) (progn (funcall func value)
                                          (travel-tree (car nodes) func order)
                                          (travel-tree (cdr nodes) func order)))
                   ((eq order 'MID) (progn (travel-tree (car nodes) func order)
                                          (funcall func value)
                                          (travel-tree (cdr nodes) func order)))
                   ((eq order 'SUF) (progn (travel-tree (car nodes) func order)
                                          (travel-tree (cdr nodes) func order)
                                          (funcall func value))))))))

;;; tree.el ends here
