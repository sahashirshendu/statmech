      program mbf
         external f
         a=1e-5
         b=1000
         n=1000
         call simpson(f,a,b,n,csi)
         write(*,*)csi
      end

      function f(x)
         m=1
         k=1
         T=1
         a=3.142**(-0.5)
         b=1
         f=2*a*x**0.5*exp(-b*x)
      end

      subroutine simpson(f, a, b, n, csi)
         h=(b-a)/n
         do i=1,n
            if (i==(i/2)*2) then
               s=s+2*f(a+i*h)
            else
               s=s+4*f(a+i*h)
            end if
         end do
         csi = h/3*(f(a)+s+f(b))
      end
