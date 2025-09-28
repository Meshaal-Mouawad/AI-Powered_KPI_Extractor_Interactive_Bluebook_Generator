Ethylene Yield %
==================================================

.. math::

   \text{}

.. raw:: html

   <style>
      .kpi-table {
         width: 100%; border-collapse: collapse; margin-bottom: 1.5em;
         border: 1px solid #e0e0e0; table-layout: fixed;
      }
      .kpi-table td {
         padding: 12px; vertical-align: top; border: 1px solid #e0e0e0;
         word-wrap: break-word;
      }
      .kpi-table td:first-child {
         width: 25%; font-weight: bold; background-color: #f7f7f7;
      }
      .kpi-table ul { list-style-type: disc; padding-left: 20px; margin: 0; }
      .kpi-table .math-equation {
         text-align: center; margin: 1em 0; overflow-x: auto; padding: 5px;
      }
      .kpi-table .formula-notes li { margin-bottom: 0.5em; }
      .kpi-table .formula-notes i { font-family: 'Times New Roman', serif; }
      .btn { display:inline-block; padding:8px 12px; border-radius:6px; color:#fff; text-decoration:none; font-weight:500; font-size:13px; }
      .btn-vscode { background-color:#2c5282; }
      .btn-pycharm { background-color:#000; }
      .btn-edit { background-color:#4a7c59; }
   </style>

   <div style="margin-bottom: 1.5em; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="font-size: 13px; font-weight: 500; color: #4a5568;">Open in:</span>
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/sql_kpi_01.sql:1" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/sql_kpi_01.sql&line=1" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=Ethylene%20Yield%20%25" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>Ethylene Yield % measures the efficiency of ethylene production by calculating the percentage of good product obtained from the total product produced</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of this KPI is to assess the effectiveness of the ethylene production process</li><li>enabling operators to identify areas for improvement and optimize production efficiency</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The formula for Ethylene Yield % is derived by dividing the quantity of good ethylene produced by the total quantity of ethylene produced, then multiplying by 100 to express it as a percentage.</p>
               <p>See code context for implementation details.</p>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               48.9s (AI 48.9s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 48.945s
                  • AI: 48.944s
                  • Render: 0.0s
               </div>
            </td>
         </tr>

         <tr>
            <td>Extraction rate %</td>
            <td>88.9%</td>
         </tr>
         <tr>
            <td>Error rate %</td>
            <td>11.1%</td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>This KPI is used in performance evaluations</li><li>production efficiency assessments</li><li>and operational benchmarking within the petrochemical industry</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for this KPI include the quantity of good ethylene produced and the total quantity of ethylene produced during a specific time frame</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for Ethylene Yield % is expressed as a percentage.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The reporting source for this KPI typically includes production data from manufacturing systems and quality control reports.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>Monitoring Ethylene Yield % is crucial for maintaining product quality and maximizing profitability in ethylene production operations.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: sql
      :linenos:
   
      :emphasize-lines: 1
   

      -- KPI: Ethylene Yield %
   -- Compute percent yield based on good product vs total product
   SELECT (good_qty * 100.0) / NULLIF(total_qty, 0) AS [Ethylene Yield %]
   FROM (
     SELECT 8200 AS good_qty, 10000 AS total_qty
   ) t;