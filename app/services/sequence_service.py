from sqlmodel import Session, select

from app.models.document_sequence import DocumentSequence


class SequenceService:

    @staticmethod
    def get_next_number(
        session: Session,
        document_type: str,
        prefix: str,
    ) -> str:

        sequence = session.exec(
            select(DocumentSequence).where(
                DocumentSequence.document_type == document_type
            )
        ).first()

        if sequence is None:

            sequence = DocumentSequence(
                document_type=document_type,
                prefix=prefix,
                last_number=1,
                digits=6,
            )

            session.add(sequence)

        else:

            sequence.last_number += 1

        return (
            f"{sequence.prefix}"
            f"{sequence.last_number:0{sequence.digits}d}"
        )