      program mbf
         external f
         a = 1e-5
         b = 1000
         n = 1000
         call simpson(f, a, b, n, csi)
         print *, csi
      end

      function f(x)
         m = 1
         k = 1
         T = 1
         c = 3.14**(-0.5)
         d = 1
         f = 2*c*x**0.5*exp(-d*x)
      end

      subroutine simpson(f, a, b, n, csi)
        h = (b - a) / n
        sum = f(a) + f(b)
        do i = 1, n
          if (i == (i / 2) * 2) then
            sum = sum + 2 * f(a + i * h)
          else
            sum = sum + 4 * f(a + i * h)
          end if
        end do
        csi = h / 3 * sum
      end
