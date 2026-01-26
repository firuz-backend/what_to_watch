dic = {
    'operation_id': int,  # 0. Split Payment 1. Fundrizing
    'queue_id': int,  # Humo id transaction
    'title': str,
    'initiator_phone': str,
    'total_amount': int,  # diram
    'partipicant': [
        {
            'phone': str,
            'amount': int,  # diram
        },

        {
            'phone': str,
            'amount': int,  # diram
        }
    ]
}


dict2 = {
    'operation_id': int,
    'request_id': int,
    'action_id': int,
}


dict3 =
[
    {
        'initiator': False,
        'request_id': int,
        'operation_id': int,
        'queue_id': int,  # Humo id transaction
        'title': str,
        'initiator_phone': str,
        'total_amount': int,  # diram
        'created_date': str,
    },

    {
        'initiator': True,
        'request_id': int,
        'operation_id': int,
        'queue_id': int,  # Humo id transaction
        'title': str,
        'initiator_phone': str,
        'total_amount': int,  # diram
        'created_date': str,
        'partipicant': [
            {
                'phone': str,
                'amount': int,  # diram
                'status': int
            }
        ]
    }
]