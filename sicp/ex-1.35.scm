;; Show that the golden ratio ф is a fixed point of the transformation
;; x -> 1 + 1/x, and use this fact to compute ф by means of the fixed-
;; point procedure.

; f(x) = 1 + 1/x
; f(x) is a fixed point => x = 1 + 1/x
;                       => x² - x - 1 = 0
;                       => (x - 1/2)² = 5/4
;                       => x - 1/2 = ±✓5/2
;                       => x = (1 ± ✓5) / 2

(define tolerance 0.00001)

(define (fixed-point f first-guess)
  (define (close-enough? v1 v2)
    (< (abs (- v1 v2)) tolerance))
  (define (try guess)
    (let ((next (f guess)))
      (if (close-enough? guess next)
        next
        (try next))))
  (try first-guess))

(display (fixed-point (lambda (x) (+ 1.0 (/ 1.0 x))) 1.0))
