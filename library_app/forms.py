from django import forms
from django.core.exceptions import ValidationError
from .models import BookReservation, BooksBorrow


class BookReservationForm(forms.ModelForm):
    class Meta:
        model = BookReservation
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        book = cleaned_data.get('book')
        status = cleaned_data.get('reservation_status')
        if book:
            if status == 'reserved':
                borrowed_count = book.borrows.filter(borrowed_status='borrowed').count()
                reserved_count = book.reservations.filter(reservation_status='reserved').count()
                total_unavailable = borrowed_count + reserved_count
                if total_unavailable >= book.stock:
                    raise ValidationError("There are no books available to reserve.")
        return cleaned_data


class BooksBorrowForm(forms.ModelForm):
    class Meta:
        model = BooksBorrow
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        book = cleaned_data.get('book')
        if book:
            borrowed_count = book.borrows.filter(borrowed_status='borrowed').count()
            reserved_count = book.reservations.filter(reservation_status='reserved').count()
            total_unavailable = borrowed_count + reserved_count
            if total_unavailable >= book.stock:
                raise ValidationError("There are no books available to borrow.")

        return cleaned_data
